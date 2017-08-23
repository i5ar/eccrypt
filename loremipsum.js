/**
 * Generate some dummy data.
 */
// Import modules
var fs = require('fs');
var mkdirp = require('mkdirp');
var loremipsum = require('lorem-ipsum');
const path = require('path');

// Make directory
var directory = 'data'
mkdirp(directory, function (err) {
  if (err) console.error(err)
  else console.log(directory + ' was made!')
});

// Save file
var files = [path.join(directory, "egg.txt"), path.join(directory, "spam.txt")]
for (var i in files) {
  fs.writeFile(files[i], loremipsum({count: 2}), function(err) {
    if(err) console.log(err)
  });
  console.log(files[i] + " was saved!")
}
