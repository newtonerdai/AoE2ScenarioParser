from __future__ import annotations

from collections import OrderedDict
from copy import deepcopy
from typing import List, Type, TYPE_CHECKING

from AoE2ScenarioParser.helper import helper
from AoE2ScenarioParser.helper.exceptions import UnsupportedAttributeError

if TYPE_CHECKING:
    from typing import OrderedDict as OrderedDictType
    from AoE2ScenarioParser.sections.retrievers.retriever_object_link import RetrieverObjectLink
    from AoE2ScenarioParser.sections.aoe2_file_section import AoE2FileSection


class AoE2Object:
    _link_list: List[RetrieverObjectLink] = []

    def __init__(self, **kwargs):
        self._instance_number_history = []
        self._sections: OrderedDictType[str, AoE2FileSection] = OrderedDict()
        self._scenario_version = None

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k != '_sections':
                val = deepcopy(v)
            else:
                val = getattr(self, k)
            setattr(result, k, val)
        return result

    @classmethod
    def _construct(cls, sections: OrderedDictType[str, AoE2FileSection], scenario_version, number_hist=None):
        if number_hist is None:
            number_hist = []

        object_parameters = {}
        for link in cls._link_list:
            object_parameters[link.name] = link.construct(sections, scenario_version, number_hist=number_hist)

            if link.support is not None and not link.support.supports(scenario_version):
                def _get(self):
                    raise UnsupportedAttributeError(f_unsupported_string(link, scenario_version))

                def _set(self, val):
                    if val is not None:
                        raise UnsupportedAttributeError(f_unsupported_string(link, scenario_version))

                setattr(cls, link.name, property(_get, _set))

        obj = cls(**object_parameters)
        obj._sections = sections
        obj._scenario_version = scenario_version

        return obj

    def commit(self, sections=None, local_link_list=None):
        """
        Commits all changes to the section & struct structure of the object it's called upon.

        Args:
            sections (OrderedDictType[str, AoE2FileSection]): A list of sections to reference where to commit to. If left empty,
                the sections default to the sections where this object was constructed from.
            local_link_list (Type[List[RetrieverObjectLink]]): a separate list of RetrieverObjectLinks. This way it's
                possible to commit only specific properties instead of all from an object.
        """
        if self._sections == {} and sections is None:
            raise ValueError("Unable to commit object. No reference to sections set.")

        if local_link_list is None:
            local_link_list = self._link_list
        if sections is None:
            sections = self._sections

        for link in local_link_list[::-1]:
            link.commit(sections, host_obj=self)

    @staticmethod
    def get_instance_number(obj: AoE2Object = None, number_hist=None) -> int:
        if obj is None and number_hist is None:
            raise ValueError("The use of the parameter 'obj' or 'number_hist' is required.")
        if obj is not None and number_hist is not None:
            raise ValueError("Cannot use both the parameter 'obj' and 'number_hist'.")

        if number_hist is None and obj is not None:
            number_hist = obj._instance_number_history
        return number_hist[-1] if len(number_hist) > 0 else None

    def __repr__(self):
        self_dict = self.__dict__
        self_dict['_sections'] = f"OrderDict"
        return str(self.__class__.__name__) + ": " + helper.pretty_print_dict(self_dict)


def f_unsupported_string(link: RetrieverObjectLink, version: str):
    return f"The property '{link.name}' is {link.support}. Current version: {version}.\n" \
           f"You can update your scenario by opening & saving it using the in-game editor of the Definitive Edition."
