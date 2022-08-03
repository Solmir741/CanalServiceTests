import './sass/style.sass'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import Urls from './components/common_components/Urls';

export const HOST = document.location.protocol + '//' + document.location.host;

function App() {
  return (
    <div>
      <Urls/>
    </div>
  );
}

export default App;