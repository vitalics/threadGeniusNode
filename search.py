import argparse

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()
parser_list = subparser.add_parser('search')
parser_list.add_argument('toFile', default=True,
                         nargs='?', help='is writing result to file')
parser_list.add_argument('gid', nargs='?', metavar='GID',
                         help='is writing result to file')
parser_list.add_argument('results', default=2 nargs='?', metavar='GID',
                         help='count of result')


parser_create = subparser.add_parser('create')
parser_create.add_argument(
    'name', default='Winter 2018', nargs='?', type=str, help='create a catalog with specific name')
parser_create.add_argument('toFile', default=True,
                           nargs='?', help='is writing result to file')


parser_get = subparser.add_parser('get')
parser_get.add_argument('gid', metavar='GID', type=str)
parser_create.add_argument('toFile', default=True,
                           nargs='?', help='is writing result to file')

parser_remove = subparser.add_parser('remove')
parser_remove.add_argument('gid', metavar='GID', type=str)
parser_create.add_argument('toFile', default=True,
                           nargs='?', help='is writing result to file')

args = parser.parse_args()
print(vars(args))
