from dependency_injector import providers, containers

from database.database import Database
from repositories.physical_stats_repository import PhysicalStatsRepository
from repositories.product_repository import ProductRepository
from repositories.user_repository import UserRepository
from services.authentication_service import AuthenticationService


class Configs(containers.DeclarativeContainer):
    dbtype = providers.Configuration('')
    username = providers.Configuration('')
    password = providers.Configuration('')
    dbname = providers.Configuration('')
class Databases(containers.DeclarativeContainer):
    database = providers.Singleton(Database,
                                   dbtype = Configs.dbtype, dbname = Configs.dbname,
                                   username = Configs.username, password = Configs.password)

class Repositories(containers.DeclarativeContainer):
    user_repo = providers.Singleton(UserRepository, database=Databases.database)
    physical_stats = providers.Singleton(PhysicalStatsRepository, database=Databases.database)
    product_repo = providers.Singleton(ProductRepository, database = Databases.database)

class Services(containers.DeclarativeContainer):
    authentication_service = providers.Singleton(AuthenticationService, Repositories.user_repo)
