// --------------------- Модуль путе по аналогии urls.py Django -----------------------------

import { BrowserRouter as Router, Redirect, Route, Switch } from 'react-router-dom';
import Order_table from '../order_table/Order_table';


// Компонент routes сюда прописываем все основные пути приложения по аналогии в urls.py



const routes = [
    {path: '/canalservice/', component: Order_table, exact: true},
    //{path: '/proba/', component: Proba, exact: true},
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
                {/*<Route path='/lk' component={() => {window.location.href = HOST}}/>*/}
                <Redirect to='//' /> {/* В случае ошибочного пути будет Rederect сюда */}
            </Switch>
        </div>
    </Router>
  )
}

export default Urls

/*
                <Route path='/staff/react/menu' exact render={() => (<Mainmenu />)} />
                <Route path='/staff/react/synonyms/word_list' exact render={() => (<SynonymsMain />)} />
                <Route path='/staff/react/synonyms/word_list/:id' component={SynonymList} />
                <Route path='/staff/react/about' component={About} />
*/
