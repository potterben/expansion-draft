//vue.config.js
module.exports = {
    chainWebpack: config => {
        config
            .plugin('html')
            .tap(args => {
                args[0].title = "NHL Expansion Draft Optimizer";
                return args;
            })
    },
    devServer: {
        host: 'localhost',
        proxy: 'http://0.0.0.0:5000/',
      }
}