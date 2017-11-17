import argparse


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='commands')

# A list command
list_parser = subparsers.add_parser('getAll', help='catalogs')
list_parser.add_argument(
    'private', default=False, action='store_false', help='Directory to list')

# a get command
list_parser = subparsers.add_parser('get', help='get catalog contents')
list_parser.add_argument('name', action='store', help='gid of catalog')
list_parser.add_argument('object', action='store',
                         help='Use this endpoint to add a list of objects to a specific catalog. Objects are added and indexed asynchronously. To check on the status of an object')

# A create command
create_parser = subparsers.add_parser('create', help='Create a catalog')
create_parser.add_argument('name', action='store',
                           help='New catalog name to create')
create_parser.add_argument('--read-only', default=False, action='store_true',
                           help='Set permissions to prevent writing to the directory',
                           )

# A delete command
delete_parser = subparsers.add_parser('delete', help='Remove a catalog')
delete_parser.add_argument('dirname', action='store',
                           help='catalog gid to remove')
delete_parser.add_argument('--recursive', '-r', default=False, action='store_true',
                           help='Remove the contents of the directory, too',
                           )

args = parser.parse_args()
print args.private
