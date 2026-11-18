export default function SearchBar({ value, onChange }) {
  return (
    <input
      className="search-bar"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder="搜尋起點或終點"
    />
  );
}