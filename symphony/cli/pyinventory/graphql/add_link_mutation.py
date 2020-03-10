#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass
from datetime import datetime
from gql.gql.datetime_utils import DATETIME_FIELD
from gql.gql.graphql_client import GraphqlClient
from functools import partial
from numbers import Number
from typing import Any, Callable, List, Mapping, Optional

from dataclasses_json import DataClassJsonMixin

from .add_link_input import AddLinkInput


@dataclass
class AddLinkMutation(DataClassJsonMixin):
    @dataclass
    class AddLinkMutationData(DataClassJsonMixin):
        @dataclass
        class Link(DataClassJsonMixin):
            id: str

        addLink: Link

    data: AddLinkMutationData

    __QUERY__: str = """
    mutation AddLinkMutation($input: AddLinkInput!) {
  addLink(input: $input) {
    id
  }
}

    """

    @classmethod
    # fmt: off
    def execute(cls, client: GraphqlClient, input: AddLinkInput) -> AddLinkMutationData:
        # fmt: off
        variables = {"input": input}
        response_text = client.call(cls.__QUERY__, variables=variables)
        return cls.from_json(response_text).data