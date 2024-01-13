export function getPage() {
	const currentURL = window.location.href;
	const urlParts = currentURL.split("/");

	return urlParts[urlParts.length - 2];	
}

export function getCookies() {
    const cookies = document.cookie.split(";");
    const cookiesObject = {};

    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        const [name, value] = cookie.split("=");
        const decodedValue = decodeURIComponent(value);
        cookiesObject[name] = decodedValue;
    }

    return cookiesObject;
}

// export function getCSRFTokenFromCookies() {
//     const cookies = getCookies();
//     console.log({ cookies })
//     if ("csrfToken" in cookies) {
//         return cookies.csrfToken;
//     }
//     return null;
// }

export function reloadPage() {
    window.location.reload();
}

export function showAlert(message) {
    const alertBox = $(".alert-box")

    alertBox.fadeIn(function() {
        $(this).text(message)
    })

    const timeOut = 1500
    setTimeout(timeOut, alertBox.fadeOut())
}

