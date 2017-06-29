module.exports = function (grunt) {
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-cssmin');

  grunt.initConfig({
    watch: {
      files: './sass/**/*.scss',
      tasks: ['sass', 'cssmin']
    },
    sass: require('./grunt_modules/sass').task,
    cssmin: require('./grunt_modules/cssmin').task
  });
};
