from authing.v2.authentication import (
    AuthenticationClient, AuthenticationClientOptions
)
from authing.v2.management import ManagementClient, ManagementClientOptions

from config import (
    AUTHING_APP_HOST, AUTHING_APP_ID, AUTHING_USERPOOL_ID,
    AUTHING_USERPOOL_SECRET
)

authentication_client = AuthenticationClient(
    options=AuthenticationClientOptions(
        app_id=AUTHING_APP_ID, app_host=AUTHING_APP_HOST
    )
)

management_client = ManagementClient(
    options=ManagementClientOptions(
        user_pool_id=AUTHING_USERPOOL_ID,
        secret=AUTHING_USERPOOL_SECRET,
    )
)

__all__ = ['authentication_client', 'management_client']
