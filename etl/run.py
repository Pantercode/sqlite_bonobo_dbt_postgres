import bonobo
from etl.graph import get_graph, get_services

if _name_ == "_main_":
    bonobo.run(get_graph(), services=get_services())
