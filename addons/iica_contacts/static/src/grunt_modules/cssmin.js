exports.task = {
  my_target: {
    expand: true,
    cwd: './css',
    src: ['*.css', '!*.min.css'],
    dest: './css',
    ext: '.min.css'
  }
};
