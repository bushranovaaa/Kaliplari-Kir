// Basit bir veri modeli örneği
const projectData = {
    mission: "Kalıpları Kır, kadınların toplumsal önyargılara karşı güçlü adımlar atmasını destekler.",
    vision: "Toplumda farkındalık yaratarak eşitlik ve fırsat eşitliğini yaygınlaştırmak.",
    goals: [
        "Kadınların hikayelerini paylaşmalarına olanak sağlamak.",
        "Gönüllülük projeleri oluşturmak.",
        "Toplumsal önyargılara karşı farkındalık kampanyaları düzenlemek."
    ]
};

// Veri modeli fonksiyonları
function getMission() {
    return projectData.mission;
}

function getVision() {
    return projectData.vision;
}

function getGoals() {
    return projectData.goals;
}

// Konsola veri modelini yazdırmak için çağrılar
console.log("Misyon:", getMission());
console.log("Vizyon:", getVision());
console.log("Hedefler:", getGoals());
