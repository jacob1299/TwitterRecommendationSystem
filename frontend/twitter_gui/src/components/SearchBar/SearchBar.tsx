import React from 'react' 

export const SearchBar = () => {
    const [search, setSearch] = React.useState()
    const handleSearch = () => {
        setSearch(search)
    }

    return (
            <div className='pt-8 mx-auto'>
                <input className='border-2 border-blue-400 rounded-lg mr-2' type='text' id='search' name='search' value={search}/>
                <button className='border-2 border-black text-white rounded-lg px-2 bg-blue-400'>Search</button>
            </div>
    )
}