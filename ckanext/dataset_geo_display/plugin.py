import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from geomet import wkt
import json


def get_geojson(dataset_wkt):
    geojson = wkt.loads(dataset_wkt)
    return json.dumps(geojson)   


class DatasetGeoDisplayPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'dataset_geo_display')
        toolkit.add_resource('assets', 'dataset_geo_display')
        
    # ITemplateHelpers

    def get_helpers(self):
        return {'get_geojson': get_geojson}
