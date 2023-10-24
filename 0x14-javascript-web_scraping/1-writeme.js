#!/usr/bin/node
const fs = require('fs/promises');
const filename = process.argv[2];

async function example() {
  try {
    const content = process.argv[3];
    await fs.writeFile(filename, content, { encoding: 'utf-8'} );
  } catch (err) {
    console.log(err);
  }
}
example();
