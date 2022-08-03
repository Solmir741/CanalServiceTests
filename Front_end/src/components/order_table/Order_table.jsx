import { HOST } from '../../App'
import logo from '../../pic/logo.png'
import axios from 'axios';
import { useEffect, useState } from 'react';


const Order_table = () => {
    const [data, setData] = useState([])
    const [total, setTotal] = useState(0)
    const [fields] = useState(['№', 'заказ №', 'стоимость, $', 'стоимость, rub', 'срок поставки'])
    const [update, setUpdate] = useState(false)

    useEffect(() => {
        const AddData = async () => {
            const article = {'passkey': '1bRT3njCRVcLayIqkMS0nCE_p_gw1ea6f5P_sLwOl9o8'};
            const urlId = HOST + '/canalservice/wr/?pk=1bRT3njCRVcLayIqkMS0nCE_p_gw1ea6f5P_sLwOl9o8'
            const request = await axios.get(urlId, article);
            const data = request.data
            setData(data.values);
            setTotal(data.total);
          };
        AddData();
    }, [update])

    useEffect(() => {
        const timeId = setTimeout(() => {
          // Обновление каждые 2 секунды
          setUpdate(!update)
        }, 2000)
    
        return () => {
          clearTimeout(timeId)
        }
      }, [update]);

    return (
        <div className='container'>
            <div className='logo'>
                <img src={logo} alt="logo" />
            </div>
            <div className="alert alert-secondary text-center total-alert" role="alert">
                <div className='total-text'>Total</div>
                <div className='total-text-sum'>{total}</div>
            </div>
            <div className="table-mediawrap scrolling" style={{marginTop: '15px'}}>
                <div className="container">
                    <table className="table table-bordered">
                        <thead>
                            <tr>
                                {fields.map((f, index) => 
                                    <th key={index}>{f}</th>
                                )}
                            </tr>
                        </thead>
                        <tbody>
                            {data.map(d => 
                                <tr key={d.id}>
                                        <td>{d.serial}</td>
                                        <td>{d.order}</td>
                                        <td>{d.cost_usd}</td>
                                        <td>{d.cost_rub}</td>
                                        <td>{d.delivery_time}</td>
                                </tr>
                            )}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

    )
}

export default Order_table