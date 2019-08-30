var position = $("#target_point").offset().top;　//最初の要素の、ドキュメント上での表示位置[y軸]を返す

$("#move_target").click(function(){
    event.preventDefault();
    $("html,body").animate({
        scrollTop : position // さっき変数に入れた位置まで
    }, {
        queue : false　// どれくらい経過してから、アニメーションを始めるか。キュー[待ち行列]。falseを指定すると、キューに追加されずに即座にアニメーションを実行。
    }, 1500, "swing");
});


