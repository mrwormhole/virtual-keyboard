package main

import (
	"fmt"
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/canvas"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/widget"
	"image/color"
)

func makeKeyboardUI() (*widget.Entry, *fyne.Container) {
	textarea := widget.NewMultiLineEntry()
	textarea.SetMinRowsVisible(3)
	buttonsContainer := container.NewAdaptiveGrid(13)

	chars := map[string][][]string{
		"UK": {
			{"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "← Backspace"},
			{"q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\"},
			{"a\ns", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "↵ Enter"},
			{"⇧", "\\", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "Space"},
		},
		"TH": {
			{"ๅ", "/", "-", "ภ", "ถ", "ุ", "ึ", "ค", "ต", "จ", "ข", "ช"},
		},
		"TR": {},
	}

	for _, line := range chars["UK"] {
		//lineContainer := container.NewHBox()

		for _, c := range line {
			btn := widget.NewButton(c, func() {
				textarea.Append(c)
			})
			btn.Alignment = widget.ButtonAlignLeading
			//lineContainer.Add(btn)
			buttonsContainer.Add(btn)

		}
		//fmt.Printf("line %d : %v\n", i, lineContainer.Size())
		//btn.Resize(fyne.NewSize(20, 20))
		//buttonsContainer.Add(lineContainer)
	}

	return textarea, buttonsContainer
}

func makeCell() fyne.CanvasObject {
	rect := canvas.NewRectangle(color.NRGBA{})
	rect.SetMinSize(fyne.NewSize(20, 20))
	return rect
}

//func NewFlexLayoutContainer(ratios []float32, objects ...fyne.CanvasObject) *fyne.Container {
//	return container.New(NewFlexLayout(ratios), objects...)
//}

//type keyboardLayout struct{}
//
//func (l *keyboardLayout) MinSize(objects []fyne.CanvasObject) fyne.Size {
//	w, h := float32(0), float32(0)
//	for _, o := range objects {
//		s := o.MinSize()
//		w += s.Width
//		h += s.Height
//	}
//	return fyne.NewSize(w, h)
//}
//
//func (l *keyboardLayout) Layout(objects []fyne.CanvasObject, containerSize fyne.Size) {
//	//pos := fyne.NewPos(0, containerSize.Width-l.MinSize(objects).Width)
//	for _, o := range objects {
//		size := o.MinSize()
//		//o.Resize(size)
//		//o.Move(pos)
//
//		//pos = pos.Add(fyne.NewPos(size.Width, size.Height))
//	}
//}

func main() {
	a := app.New()
	w := a.NewWindow("Virtual Keyboard")

	textarea, buttonsContainer := makeKeyboardUI()

	mainContainer := container.NewBorder(makeCell(), makeCell(), makeCell(), makeCell())

	mainContainer.Add(container.New(layout.NewVBoxLayout(), textarea, buttonsContainer))

	//w.Resize(fyne.NewSize(400, 300))

	w.SetContent(mainContainer)

	fmt.Println(w.Canvas().Size())

	w.ShowAndRun()
}
