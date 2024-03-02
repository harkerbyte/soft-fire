const path = require('path');
const glob = require('glob');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports={
    mode:'production',
    entry:{
        js_file : glob.sync('./uploads/ts/*.ts'),
        css_file : glob.sync('./uploads/scss/*.scss'),
    },
    output:{
        path : path.resolve(__dirname, './download'),
        filename:'[name].js',
    },
    module:{
        rules:[
            {
                test:/\.ts$/,
                use:'ts-loader',
                exclude:/node_modules/,
            },
            {
                test:/\.scss$/,
                use:[
                    MiniCssExtractPlugin.loader,
                    {
                        loader:'css-loader',
                    },
                    {
                        loader:'sass-loader',
                    },
                ],
                exclude:/node_modules/,
            },
        ],
    },
    resolve:{
        extensions:['.ts','.js']
    },
    plugins:[
        new MiniCssExtractPlugin({
            filename:'[name].css',
        }),
    ],
}