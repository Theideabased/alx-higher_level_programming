#!/usr/bin/node

const fs = require('fs/promises');
const filename = process.argv[2];

async function example () {
  try {
    const data = await fs.readFile(filename, { encoding: 'utf8' });
    console.log(data);
  } catch (err) {
    console.log(err);
  }
}
example();
