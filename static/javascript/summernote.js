let checkUnload = true;
$(window).on('beforeunload', function () {
    if (checkUnload) return "이 페이지를 벗어나면 작성된 내용은 저장되지 않습니다.";
});
$("#write").on("click", function () {
    checkUnload = false;
    $("submit").submit();
});

$(document).ready(function () {
    $("img").addClass("img-responsive");
    $("img").css("max-width", "100 %");
});