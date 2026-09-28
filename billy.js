function toggleMode(){
    document.getElementById("body").classList.toggle("dark");
}

<script>
    cont originalTitle = document.title;

    document.addEventListener("visibilitychange", () => {
        document.title = document.hidden ?
        "Come back :(" :
        originalTitle ;
    });
</script>