const merge = require('webpack-merge')
const common = require('./webpack.common.js')
const RelativeBundleTrackerPlugin = require('./RelativeBundleTrackerPlugin')

module.exports = merge(common, {
    mode: 'production',
    devtool: false,
    plugins: [
        new RelativeBundleTrackerPlugin({
            path: __dirname,
            filename: './webpack-stats-prod.json'
        })
    ]
})
