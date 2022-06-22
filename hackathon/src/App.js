import React,{useState, useEffect} from 'react'

function App() {

  const [data,setData]= useState([{}])

  useEffect(()=>{
    fetch("/projet").then(
      res=>res.json()
    ).then(
      data=>{
        setData(data)
        console.log(data)
      }
    )
  },[])
  return (
    <div>
      {data.jobs.map(job =>(
        <p key={job.id}>{job.id} : {job.name}</p>
      ))}
    </div>
  )
}

export default App