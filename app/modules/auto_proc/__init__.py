"""ISPyB flask server"""

from app.models import AutoProc as AutoProcModel
from app.modules import auto_proc

def get_auto_proc_list():
    auto_proc_list = AutoProcModel.query.all()
    return auto_proc.schemas.ma_auto_proc_schema.dump(auto_proc_list)
