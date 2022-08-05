
import { BrowserRouter as Router, Redirect, Route, Switch } from 'react-router-dom';
import Order_table from '../order_table/Order_table';




const routes = [
    {path: '/canalservice/', component: Order_table, exact: true},
]

const Urls = () => {
  return (
    <Router>
        <div className="App">
            <Switch>
                {routes.map(route =>
                    <Route key={route.path}
                        component={route.component}
                        path={route.path}
                        exact={route.exact}
                    />)}
            </Switch>
        </div>
    </Router>
  )
}

export default Urls

