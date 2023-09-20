class Square extends React.Component {
  render() {
    return (
      <button className="square" onClick={()=> this.props.onClick()}>
        {this.props.bold ? <b>{this.props.value}</b>: this.props.value}
      </button>
    );
  }
  
}

class Board extends React.Component {
  renderSquare(i, bold) {
    return <Square key={i} value={this.props.squares[i]} bold={bold} onClick={()=> this.props.onClick(i)}/>; 
  }
  renderBoard(){
    let boards = []
    for(let i=0; i< 9; i=i+3){
      let temp = []
      for(let j=i; j<i+3;j++){
          if(this.props.winner.includes(j)){    
             temp.push(this.renderSquare(j, true))
           }
           else{
              temp.push(this.renderSquare(j, false))  
           }
           
      }
      boards.push(<div key={i} className="board-row"> {temp} </div>)
    }
    return boards;
  }
  render() {
    return (
      <div>
        <div className="status">{status}</div>
        {this.renderBoard()}
      </div>
    );
  }
}

class Game extends React.Component {
  
  constructor(props){
    super(props);
    this.state = {
      history : [{"squares": Array(9).fill(null)}],
      xIsNext: true,
      stepNumber: 0,
      asc:true
    }
  }
  
  handleClick(i){
    const history = this.state.history.slice(0, this.state.stepNumber+1)
    const current = history[history.length-1]
    let squares = current.squares.slice()
    const winner = calculateWinner(squares)
    if(winner || squares[i] != null){
      return; 
    }
    let xIsNext = this.state.xIsNext
    squares[i] = "X"
    if (!xIsNext){
      squares[i] = "O"
    }
    xIsNext = !xIsNext
    history.push({"squares": squares})
    this.setState({
      history : history,
      xIsNext : xIsNext,
      stepNumber: history.length-1
    });
  }
  
  handleHistory(move){
    this.setState({
      stepNumber: move,
      xIsNext : (move%2)===0
    });
    
  }
  handleSort(){
    let asc = this.state.asc
    asc = !asc
    this.setState({
      asc : asc
    });
  }
  renderMove(history, asc){
    let moves = history.map((step, move)=>{
        let dest = move ? `go to move ${move}` : `go to start`
        return (
          <li key={move}>
            <button onClick={()=>{this.handleHistory(move)}}>{ this.state.stepNumber == move ? <b> {dest} </b> :  dest}</button>
          </li>
        )
    })
    moves =  asc ? moves : moves.reverse(); moves
    return moves;
  }
  
  render() {
    
    const history = this.state.history
    let step = this.state.stepNumber
    const current = history[this.state.stepNumber]
    const squares = current.squares
    
    let status = 'Next player: X';
    
    let moves = null;
    if(this.state.asc){
      moves = this.renderMove(history, true);  
    }
    else{
      moves = this.renderMove(history, false)
    }
    
    if(!this.state.xIsNext){
      status = "Next player: O"
    }
    let winner = calculateWinner(squares)
    if (winner){
        status = this.state.xIsNext ? "Winner : O" : "Winner: X";
    }
    let draw_null = squares.some(x=> x===null) 
    if(!draw_null && !winner){
      status = "Game Draw"
    }
    return (
      <div className="game">
        <div className="game-board">
          <Board squares= {squares} winner={winner? winner: []} onClick={(i)=> this.handleClick(i)}/>
        </div>
        
        <div className="game-info">
          <div>{status}</div>
          <ol>{moves}</ol>
        </div>
        <div className="game-info">
          <button onClick={()=>{this.handleSort()}}>sort</button>
        </div>
      </div>
    );
  }
}

// ========================================

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Game />);

function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a], [a,b,c];
    }
  }
  return null, null;
}