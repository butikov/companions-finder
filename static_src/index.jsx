import React from 'react';
import ReactDOM from 'react-dom';
import createHistory from 'history/createBrowserHistory';
import { ConnectedRouter, routerMiddleware } from 'react-router-redux';
import {Provider} from 'react-redux';

import App from './components/App'
import initStore from './utils/store'

const history = createHistory();
const middleware = routerMiddleware(history);



ReactDOM.render(
//    <Provider store={ initStore([middleware]) }>
//        <ConnectedRouter history={ history }>
            <App />,
//        </ConnectedRouter>
//    </Provider>,
    document.getElementById('root'),
);