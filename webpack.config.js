const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

const NODE_ENV = process.env.NODE_ENV || 'development';

module.exports = {
    entry: {
//        testBundle: './test',
        indexBundle: './index',
//        testRedux: './testRedux',
    },
    context: `${__dirname}/static_src`,
    output: {
        path: `${__dirname}/static/build`,
        filename: NODE_ENV ? '[name].js' : '[name]-[hash].js',
        publicPath: '/static/build/',
    },

    plugins: [
//            new webpack.NoEmitOnErrorsPlugin(),
            new BundleTracker({filename: './webpack-stats.json'}),
        ],

    resolve: {
        modules: [`${__dirname}/static_src`, 'node_modules'],
        extensions: ['.js', '.jsx'],
    },

    watch: NODE_ENV === 'development',
    watchOptions: {
        aggregateTimeout: 100,
    },

    module:{
        rules: [
            {
                test: /\.(js|jsx)$/,
                include: `${__dirname}/static_src`,
                loader: 'babel-loader?presets[]=react&presets[]=env&presets[]=stage-1',
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader',
            },
            {
                test: /\.scss$/,
                loader: 'style-loader!css-loader!sass-loader?outputStyle=expanded',
            },
            {
              test: /\.(png|jpg|gif|svg|ttf)$/,
                loader: 'url-loader?limit=4096&name=[path][name].[ext]',
            },

        ],
    },

    devtool: NODE_ENV === 'development' ? 'cheap-inline-module-source-map' : false,

};

if (NODE_ENV !== 'development'){
    module.exports.plugins.push(
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: false,
                drop_console: true,
                unsafe: true,
            }
        })
    )
}