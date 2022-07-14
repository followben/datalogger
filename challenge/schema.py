import graphene

from challenge.datalogger import mutations as dataloggermutations
from challenge.datalogger import queries as dataloggerqueries


class Query(dataloggerqueries.Query):
    """Container class for all app Query mixins"""


class Mutation(dataloggermutations.Mutation):
    """Container class for all app Mutation mixins"""


schema = graphene.Schema(query=Query, mutation=Mutation)
