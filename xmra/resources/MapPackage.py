import json
from xmra.repositories.local.db import session
from xmra.repositories.local import model
from xmra.xonotic.objects import MapPackage
from xmra.util import ObjectEncoder
from xmra.util import DateTimeEncoder


class MapPackageResource:

    def on_get(self, req, resp):
        """Handles GET requests"""
        print(req.params)

        q = session.query(model.MapPackage)
        map_packages = []
        for map_package in q:
            print(map_package)
            # map_package = MapPackage(
            #     pk3_file=map_package.pk3_file
            # )
            # map_packages.append(map_package.to_json())
            r_map_package = {
                'map_id': map_package.map_package_id,
                'pk3_file': map_package.pk3_file,
                'shasum': map_package.shasum,
                'date': map_package.date,
            }
            map_packages.append(r_map_package)

        resp.body = json.dumps(map_packages, cls=DateTimeEncoder)

    def on_post(self, req, resp):
        """Handles GET requests"""
        print(req.params)
        map_package = model.MapPackage(**req.params)
        session.add(map_package)
        session.commit()
