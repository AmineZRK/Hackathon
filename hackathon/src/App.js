import React,{useState, useEffect} from 'react'
import axios from 'axios'
function App() {

  const [data,setData]= useState([{}])
  const [info,setInfo]= useState([{}])

  useEffect(()=>{
    fetch("/project").then(
      res=>res.json()
    ).then(
      data=>{
        setData(data)
        console.log(data)
      }
    )
  },[]);

 
  const handleClick = (id) => {
    fetch(`/members/${id}/`,{
      headers : { 
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }

    })
            .then(
              res=>res.json()
            ).then(
              info=>{
                setInfo(info)
                console.log(info)
              }
            )
            
  }
  return (
    <div>
      {(typeof data.projects === 'undefined')?(
        <h1>Loading...</h1>
      ) :(
        data.projects.map(projet =>(
          <a href='#' onClick={() => handleClick(projet.id)}>
            <p key={projet.name}>{projet.id} : {projet.name}</p>
          </a>
        ))
      )}
    </div>
  )
     
  }
 

export default App