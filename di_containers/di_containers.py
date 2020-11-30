from dependency_injector import providers, containers

from database.database import Database
from repositories.physical_stats_repository import PhysicalStatsRepository
from repositories.product_repository import ProductRepository
from repositories.user_repository import UserRepository
from services.physical_stats_service import PhysicalStatsService
from services.product_service import ProductService
from services.user_service import UserService


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
    physical_stats_repo = providers.Singleton(PhysicalStatsRepository, database=Databases.database)
    product_repo = providers.Singleton(ProductRepository, database = Databases.database)

class Services(containers.DeclarativeContainer):
    user_service = providers.Singleton(UserService, Repositories.user_repo)
    physical_stats_service = providers.Singleton(PhysicalStatsService,
                                                 Repositories.physical_stats_repo,
                                                 Repositories.user_repo
                                                 )
    product_service = providers.Singleton(ProductService,Repositories.product_repo)
