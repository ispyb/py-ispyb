"""ISPyB flask server"""

from app.models import AutoProcIntegration as AutoProcIntegrationModel
from app.modules.auto_proc_integration.schemas import (
    f_auto_proc_integration_schema,
    ma_auto_proc_integration_schema,
)


def get_auto_proc_integration_list():
    auto_proc_integration_list = AutoProcIntegrationModel.query.all()
    return ma_auto_proc_integration_schema.dump(auto_proc_integration_list)
