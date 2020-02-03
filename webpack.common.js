const MiniCssExtractPlugin = require("mini-css-extract-plugin")
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const BundleTracker = require('webpack-bundle-tracker')
const appName = 'workshop'
const path = require("path")


module.exports = {
    entry: {
        vuejs: './' + appName + '/static/vue/main.js',
    },
    output: {
        path: path.resolve('./' + appName + '/static/bundles/'),
        filename: '[name]-[hash].js',
    },
    plugins: [
        new VueLoaderPlugin(),
        new BundleTracker({
            path: __dirname,
            filename: './webpack-stats.json'
        }),
        new MiniCssExtractPlugin({
            filename: '[name]-[hash].css',
            chunkFilename: '[id].css',
        }),
    ],
    module: {
        rules: [{
                test: /\.scss$/,
                use: [{
                        loader: MiniCssExtractPlugin.loader,
                    },
                    {
                        loader: "css-loader"
                    },
                    {
                        loader: "sass-loader",
                    }
                ]
            },
            {
                test: /\.css$/,
                use: ['vue-style-loader', 'css-loader']
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader',
                options: {
                    loaders: {
                        css: 'css-loader'
                    }
                }
            }
        ]
    }
}
