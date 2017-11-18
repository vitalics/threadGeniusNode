import sys
import json
from threadgenius import ThreadGenius
from threadgenius.types import CatalogObject, ImageUrlInput
import argparse

parser = argparse.ArgumentParser(description='TheadGenius API caller.')
parser.add_argument('getCatalogs',  nargs='?', help='get all catalogs')
parser.add_argument('catalogName', nargs='?',
                    help='get catalog by id', type=str)

tg = ThreadGenius(api_key='key_MzhiNWI4YTJiYzQ4Yjc2ZWVhZjRhMTQ4ZWI4MTUw')
# catalog_73e3d645bd734e115b6c98ab80de8b

args = parser.parse_args()

if args.getCatalogs:
    file = open(args.getCatalogs + ".json", "w")
    # print 'executing getCatalogs'

    response = tg.list_all_catalogs()
    formattedJson = json.dumps(response, indent=4, sort_keys=True)
    file.write(formattedJson)
    file.close()

    # print 'getCatalogs finished successfull'

if args.catalogName:
    # print args.catalogName
    # print 'executing get catalog by gid'
    catalog_gid = args.catalogName
    file = open(catalog_gid + '.json', "w")
    response = tg.get_catalog(catalog_gid=catalog_gid)
    formattedJson = json.dumps(response, indent=4, sort_keys=True)
    file.write(formattedJson)
    file.close()

    # print 'get catalogs by gid finished successfull'
