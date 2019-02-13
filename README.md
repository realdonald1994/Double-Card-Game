# comp6721
counter four





## Test results (Double-Card-2nd-Version):

| command input  | configuration image | test result | comments |
|----------------|:--------------------|:------------|:---------|
|  dots <br> 0 1 A 2  | <img src="test_result_images/configuration-1-test-hanging-position.jpg" width="380">  | 测试通过 | 测试放置悬空的卡片 |
|  dots <br> 0 1 A 1 <br> 0 1 B 2 | <img src="test_result_images/configuration-2-test-hanging-position.jpg" width="380">  | 测试通过  | 测试放置悬空的卡片  |
|  dots <br> 0 1 H 1 | <img src="test_result_images/configuration-3-test-out-of-board-x-position.jpg" width="380">  | 测试通过  | 测试卡片片段超出board x轴情况  |
|  dots <br> 0 2 B 1 <br> 0 4 A 1 <br> 0 1 A 3 <br> 0 2 B 4 <br> 0 8 A 4 <br> 0 6 A 6 <br> 0 4 A 8 <br> 0 2 A 10 <br> 0 2 A 12 | <img src="test_result_images/configuration-4-test-out-of-board-y-position.jpg" width="380">  | 测试通过  | 测试卡片片段超出board y轴情况  |
|  dots <br> 0 5 A 1 <br> 0 2 A 2 <br> 0 6 D 1 <br> 0 4 B 2 <br> 0 8 C 1 <br> 0 7 C 3 <br> 0 1 A 4 <br> 0 7 C 4 <br> 0 6 C 5 | <img src="test_result_images/configuration-5-player1-wins.jpg" width="380">  | Failed | 测试在player1放置0 6 C 5卡片后，player1和player2同时满足赢的状态下，判定player1赢 |
|   |   |   |   |

in configuration images:
> **Blue square** means the piece that player1 drops

> **Orange square** means the piece that player2 drops

> **Green square** means that the winning position.
