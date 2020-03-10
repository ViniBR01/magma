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

from gql.gql.enum_utils import enum_field
from .property_kind_enum import PropertyKind

from .service_type_create_data_input import ServiceTypeCreateData


@dataclass
class AddServiceTypeMutation(DataClassJsonMixin):
    @dataclass
    class AddServiceTypeMutationData(DataClassJsonMixin):
        @dataclass
        class ServiceType(DataClassJsonMixin):
            @dataclass
            class PropertyType(DataClassJsonMixin):
                id: str
                name: str
                type: PropertyKind = enum_field(PropertyKind)
                index: Optional[int] = None
                stringValue: Optional[str] = None
                intValue: Optional[int] = None
                booleanValue: Optional[bool] = None
                floatValue: Optional[Number] = None
                latitudeValue: Optional[Number] = None
                longitudeValue: Optional[Number] = None
                isEditable: Optional[bool] = None
                isInstanceProperty: Optional[bool] = None

            id: str
            name: str
            hasCustomer: bool
            propertyTypes: List[PropertyType]

        addServiceType: ServiceType

    data: AddServiceTypeMutationData

    __QUERY__: str = """
    mutation AddServiceTypeMutation($data: ServiceTypeCreateData!) {
  addServiceType(data: $data) {
    id
    name
    hasCustomer
    propertyTypes {
      id
      name
      type
      index
      stringValue
      intValue
      booleanValue
      floatValue
      latitudeValue
      longitudeValue
      isEditable
      isInstanceProperty
    }
  }
}

    """

    @classmethod
    # fmt: off
    def execute(cls, client: GraphqlClient, data: ServiceTypeCreateData) -> AddServiceTypeMutationData:
        # fmt: off
        variables = {"data": data}
        response_text = client.call(cls.__QUERY__, variables=variables)
        return cls.from_json(response_text).data