var PythonShell = require('python-shell');
var options = {
    mode: 'text',
    // pythonOptions: ['-u'],
    scriptPath: __dirname + '/theadgenius.py',
    args: ['getCatalogs', 'catalog_73e3d645bd734e115b6c98ab80de8b']
};


PythonShell.run('', options, function (err) {
    if (err) throw err;
    console.log('finished');
});