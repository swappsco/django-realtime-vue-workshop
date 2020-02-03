const merge = require("webpack-merge");
const common = require("./webpack.common.js");
const RelativeBundleTrackerPlugin = require("webpack-bundle-tracker");

module.exports = merge(common, {
    mode: "development",
    devtool: "inline-source-map",
    plugins: [
        new RelativeBundleTrackerPlugin({
            path: __dirname,
            filename: "./webpack-stats.json"
        })
    ]
});
