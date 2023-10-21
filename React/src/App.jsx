import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <div>
      <h1 className='text-xl font-bold text-center'>This is a fastapi based react webdevelopment project</h1>
     </div>
    </>
  )
}

export default App
