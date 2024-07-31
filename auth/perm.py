from casbin import AsyncEnforcer
from casbin.util import key_match2
from casbin_async_sqlalchemy_adapter import Adapter
from fastapi import Depends, HTTPException

from auth.user import decode_token
from config import DEBUG
from database import engine
from models.user import UserDB

adapter = Adapter(engine)
enforcer = AsyncEnforcer('./casbin.conf', adapter, enable_log=DEBUG)
enforcer.enable_auto_save(True)
enforcer.add_named_matching_func('g', key_match2)
enforcer.add_named_domain_matching_func('g', key_match2)


def require_permission(resource: str, action: str, domain: str = 'default'):
    """要求某个资源的某种权限

    Args:
        resource: 资源
        action: 对资源进行的操作
        domain: 域（一般指定成学校的 id，按 school_{school_id} 格式化后传入）

    Raises:
        HTTPException: 没有权限（或者上游依赖项错误）

    Returns:
        一个依赖项，执行后返回用户
    """

    async def wrapper(user: UserDB = Depends(decode_token)):
        nonlocal resource, action, domain

        await enforcer.load_policy()  # 反正这段代码是 async 的（而且这软件也不追求高并发）
        if not enforcer.enforce(resource, domain, f'user_{user.id}', action):
            raise HTTPException(403, detail='Permission denied')
        return user

    return wrapper


__all__ = ['enforcer']
