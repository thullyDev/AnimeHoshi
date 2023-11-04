import { useState } from 'react'
import './App.css'

const reactLogo = "react.svg"
const viteLogo = "vite.svg"

const reactLogoPath = `/static/${reactLogo}`
const viteLogoPath = `/static/${viteLogo}`

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogoPath} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogoPath} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React + Django</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
