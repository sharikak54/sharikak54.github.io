class Square1 {
  state = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]];
  isTilted = [0, 0];

  parseMoves(moveStr) {
    if (moveStr.indexOf("/") === 0) {
      moveStr = "0,0" + moveStr;
    }
    if (moveStr.charAt(moveStr.length - 1) === "/") {
      moveStr = moveStr + "0,0";
    }

    let moves = moveStr.split("/");
    let prunedMoves = moves.reduce((carry, move) => {
      if (move && move.indexOf(",")) {
        move = move.split(",");
        carry.push([parseInt(move[0]), parseInt(move[1])]);
        return carry;
      }
    }, [])
    
    return prunedMoves;
  }

  doMoves(moveStr) {
    const moves = this.parseMoves(moveStr);
    console.log(moves);
    for (var i = 0; i < moves.length; i++) {
      this.ud(moves[i]);
      if (i !== moves.length - 1) {
        this.doSlash();
      }
    }
  }

  getState() {
    return [[...this.state[0]], [...this.state[1]]];
  }

  /** Apply a move [u,d] to the top and bottom face. */
  ud(move) {
    // Error checking and prep rotations
    const rots = [...move];
    for (let i = 0; i < 2; i++) {
      rots[i] = (rots[i] + 12) % 12;
      const newTilt = (this.isTilted[i] + rots[i]) % 3;
      if (i + newTilt === 2) {
        throw new Error("Can't leave tilt at 2 :(");
      }
      this.isTilted[i] = newTilt;
    }

    // Apply rotations
    for (let i = 0; i < 2; i++) {
      let rot = rots[i];
      rot = Math.floor(rot / 3);
  
      let side = this.state[i];
      for (let j = 0; j < rot; j++) {
        side = [...side.slice(6), ...side.slice(0, 6)];
      }
      this.state[i] = side;
    }
  }

  /** Attempt to apply a "/" move to the current state. */
  doSlash() {
    // error checking
    if (this.isTilted[0] % 3 !== (1 + this.isTilted[1]) % 3) {
      throw new Error("wrong tilt!");
    }

    const top = this.state[0];
    const bot = this.state[1];
    
    // TODO check tiltedness to determine which pieces to swap
    let topRightHalf = top.slice(4);
    for (let i = 4; i < 8; i++) {
      top[i] = bot[i];
      bot[i] = topRightHalf[i - 4];
    }
  }

}