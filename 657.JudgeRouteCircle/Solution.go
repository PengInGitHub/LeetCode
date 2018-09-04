func judgeCircle1(moves string) bool {
	start := [2]int{0, 0}
	for _, move := range moves {
		switch move {
		case 'L':
			start[0] = start[0] - 1
		case 'R':
			start[0] = start[0] + 1
		case 'U':
			start[1] = start[1] - 1
		case 'D':
			start[1] = start[1] + 1
		}
	}
	if start[0] == 0 && start[1] == 0 {
		return true
	}
	return false
}

func judgeCircle2(moves string) bool {
	x, y := 0, 0
	if len(moves)%2 != 0 {
		return false
	}
	for _, move := range moves {
		switch move {
		case 'U':
			y--
		case 'D':
			y++
		case 'L':
			x--
		case 'R':
			x++
		}
	}
	if x == 0 && y == 0 {
		return true
	}
	return false
}

func judgeCircle(moves string) bool {
	if len(moves)%2 != 0 {
		return false
	}
	x, y := 0, 0
	mapX := map[string]int{"L": -1, "R": 1}
	mapY := map[string]int{"U": -1, "D": 1}
	for _, move := range moves {
		x += mapX[string(move)]
		y += mapY[string(move)]
	}
	if x == 0 && y == 0 {
		return true
	}
	return false
}




