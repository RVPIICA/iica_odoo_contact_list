
exports.task = {
  dist: {
    options: {
      style: 'expanded',
      lineNumbers: true,
      sourcemap: 'none'
    },
    files: [{
      expand: true,
      cwd: './sass',
      src: ['**/*.scss'],
      dest: './css',
      ext: '.css'
    }]
  }
};
