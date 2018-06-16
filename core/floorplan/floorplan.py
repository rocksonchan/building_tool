import bpy
import bmesh

from .floorplan_types import (
    fp_rectangular,
    fp_circular,
    fp_composite,
    fp_hshaped,
    fp_random
    )

from ...utils import (
    link_obj,
    make_mesh,
    bm_to_obj,
    make_object,
    bm_from_obj,
    kwargs_from_props,
    )


class Floorplan:

    @classmethod
    def build(cls, context, props):
        """Use floorplan types and properties to generate geometry

        Args:
            context (bpy.context): blender context
            props (bpy.types.PropertyGroup): FloorplanProperty
        """
        obj = make_object('floorplan', make_mesh('fp_mesh'))
        bm = bm_from_obj(obj)

        kwargs  = kwargs_from_props(props)
        if props.type == 'RECTANGULAR':
            fp_rectangular(bm, **kwargs)

        elif props.type == 'CIRCULAR':
            fp_circular(bm, **kwargs)

        elif props.type == 'COMPOSITE':
            fp_composite(bm, **kwargs)

        elif props.type == 'H-SHAPED':
            fp_hshaped(bm, **kwargs)

        elif props.type == 'RANDOM':
            fp_random(bm, **kwargs)

        bm_to_obj(bm, obj)
        link_obj(obj)
