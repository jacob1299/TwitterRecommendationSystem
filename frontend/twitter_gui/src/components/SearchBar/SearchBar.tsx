import React from 'react' 

export const SearchBar = () => {
    const [search, setSearch] = React.useState<any>('')

    
    const handleSubmit = () => {
        post_query(search)
        console.log(search)
    }

  async function post_query(search: any) {
        const response = await fetch('http://localhost:5000/api/search_query', {
            method: 'POST', 
            mode: 'cors', 
            cache: 'no-cache', 
            credentials: 'same-origin', 
            headers: {
              'Content-Type': 'application/json'
            },
            redirect: 'follow',
            referrerPolicy: 'no-referrer', 
            body: JSON.stringify(search)
          }).then(response => console.log(response))
    }



    return (
            <div className='pt-8 mx-auto'>
                <h1>{search}</h1>
                <input className='border-2 border-blue-400 rounded-lg mr-2' type='text' id='search' name='search' value={search} onChange={e => setSearch(e.target.value)}/>
                <button className='border-2 border-black text-white rounded-lg px-2 bg-blue-400' onClick={() => handleSubmit()}>Search</button>
            </div>
    )
}