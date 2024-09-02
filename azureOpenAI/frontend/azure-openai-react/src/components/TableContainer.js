import React, { useState } from "react"
import axios from 'axios';
import tableData from "../resources/tableData.json";
import "../styles/TableContainer.css";

const TableContainer = () => {

    const [state, setState] = useState({data: tableData})

    const getDetailData = async (index) =>{
        if(!state.data[index].detail){
            let tempData = state.data;
            let companyName = tempData[index].companyName;
            try {
                const res = await axios.post('http://localhost:5000/api/companySummary', { companyName });
                tempData[index].detail = JSON.parse(res.data.response);
                setState({data: tempData});
            } catch (error) {
                console.error(error);
            }
        }
    }

    return(
        <>
            <table>
                <thead>
                    <tr>
                        <td>companyName</td>
                        <td>projectName</td>
                        <td>submissionDate</td>
                        <td>contactMail</td>
                        <td>contactName</td>  
                    </tr>
                </thead>
                <tbody>
                    {state.data?.map((item,index)=>(
                        <>
                            <tr key={(2*index)-1}>
                                <td className="company-name" onClick={()=> getDetailData(index)}>{item.companyName}</td>
                                <td>{item.projectName}</td>
                                <td>{item.submissionDate}</td>
                                <td>{item.contactMail}</td>
                                <td>{item.contactName}</td>
                            </tr>
                            <tr className={`detail ${item.detail? "":"hidden"}`} key={2*index}>
                                <td colSpan="5">
                                    <div>
                                        <h3>¿Qué sabes sobre {item.companyName}?</h3>
                                        <p>{item.detail && item.detail.choices && item.detail.choices[0].message.content}</p>
                                    </div>
                                </td>
                            </tr>
                        </>
                    ))}
                </tbody>
            </table>
        </>
    )
}

export default TableContainer;