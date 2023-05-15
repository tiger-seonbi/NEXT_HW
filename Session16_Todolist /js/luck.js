const lucks = [
    "오늘은 운명같은 사람을 만날 수 있는 날입니다. 마음의 준비를 해두세요.",
    "오늘은 코딩하기에 머리가 돌아가지 않는 날입니다. 조금 쉬세요.",
    "오늘은 누군가 당신에게 야식을 사주는 날입니다. 메뉴를 생각해두세요.",
    "오늘은 모든 일이 술술 풀리는 날입니다. 새로운 도전을 해보세요.",
    "오늘은 조금씩 어긋나는 날입니다. 중요한 일을 나중으로 미뤄보세요.",
    "오늘은 주량이 일시적으로 늘어난 날입니다. 술배틀에 참여해보세요.",
  ];
  
  const luck = document.querySelector("#luck p");
  const luckToday = lucks[Math.floor(Math.random() * lucks.length)];
  luck.innerText = luckToday;